var globals = {
    urlAPI: import.meta.env.VITE_API_URL, // dev "http://localhost:5333/api/",
    urlBASE: import.meta.env.VITE_BASE_URL,// dev "http://localhost:5333/",
    getUrl: function (path) {
        return this.urlAPI + path
    }
}
export default globals