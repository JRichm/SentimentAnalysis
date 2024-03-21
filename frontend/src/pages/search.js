export default function SearchPage() {
    return (
        <div className="bg-slate-700 min-h-screen flex flex-col place-items-center pt-14">
            <div className="w-[800px] flex flex-col place-items-center">
                <h1 className="text-white text-[40px] font-thin italic">Youtube Comment Sentiment Analysis</h1>
                <div className="w-full">
                    <form className="flex flex-row w-full justify-between place-items-center border border-black rounded-full p-2 bg-slate-800/20">
                        <input className="bg-transparent w-full outline-none p-1 px-4 text-white" placeholder="paste youtube link..."></input>
                        <button>
                            <i class="fa-solid fa-magnifying-glass text-white p-3"></i>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}