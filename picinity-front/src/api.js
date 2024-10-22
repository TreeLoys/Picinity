var api = {
    apiURL: "http://localhost:5333",
    get: async (url, params) => {
        if (url.startsWith("/"))
            url = this.apiURL += url
        let response = await fetch(url)
        if (response.ok)
            return await response.json()
        else
            throw `Error at GET to api url: ${url}`
    },
    post: async (url, params) => {
        if (url.startsWith("/"))
            url = this.apiURL += url
        let response = await fetch(url,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(params)
            }
        )
        if (response.ok)
            return await response.json()
        else
            throw `Error at POST to api url: ${url}`
    }
}
export default api