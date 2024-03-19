function App() {
  return (
    <div className="bg-slate-700 min-h-screen flex flex-col place-items-center pt-14">
      <form className="p-4 w-[400px] bg-slate-300 rounded-lg border-4 border-slate-500">
        <div className="flex flex-col">
          <label className="font-medium">Input</label>
          <input className="mb-4" type="text"></input>
          <label className="font-medium">Number</label>
          <input className="mb-4" type="number"></input>
          <span className="flex justify-between">
            <label className="font-medium">Checkbox</label>
            <input className="mb-4" type="checkbox"></input>
          </span>
          <input className="bg-green-500 text-white rounded place-self-end px-6" type="submit"></input>
        </div>
      </form>
    </div>
  );
}

export default App;
