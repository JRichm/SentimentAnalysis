import React, { useState, useEffect } from 'react'

export default function TestFormPage() {
    const [formData, setFormData] = useState({ text: '', number: 0, checkbox: false })
    const [csrfToken, setCsrfToken] = useState('')
    
    useEffect(() => {
        async function fetchCsrfToken() {
            try {
                const response = await fetch('/api/get_csrf_token')
                const { csrfToken } = await response.json()
                setCsrfToken(csrfToken)
            } catch (error) {
                console.error('Error fetching CSRF token: ', error)
            }
        }
        fetchCsrfToken()
    }, [])
    
    const handleChange = (event) => {
        const { name, value, checked, type } = event.target
        const val = type === 'checkbox' ? checked : value
        setFormData({
            ...formData,
            [name]: val
        })
    }
    
    const handleSubmit = async (event) => {
        event.preventDefault()
        try {
            const response = await fetch('/api/testformendpoint/', {
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
                },
                body: JSON.stringify(formData),
            })
        
            const responseData = await response.json()
            alert("API response: " + JSON.stringify(responseData.data));
        } catch (err) {
            alert(err)
        }
    }
    
    return (
        <div className="bg-slate-700 min-h-screen flex flex-col place-items-center pt-14">
            <form className="p-4 w-[400px] bg-slate-300 rounded-lg border-4 border-slate-500" onSubmit={handleSubmit}>
                <div className="flex flex-col">
                <label className="font-medium">Input</label>
                <input className="mb-4" type="text" name="text" value={formData.text} onChange={handleChange}></input>
                <label className="font-medium">Number</label>
                <input className="mb-4" type="number" name="number" value={formData.number} onChange={handleChange}></input>
                <span className="flex justify-between">
                    <label className="font-medium">Checkbox</label>
                    <input className="mb-4" type="checkbox" name="checkbox" checked={formData.checkbox} onChange={handleChange}></input>
                </span>
                <input className="bg-green-500 text-white rounded place-self-end px-6" type="submit"></input>
                </div>
            </form>
        </div>
    );
}