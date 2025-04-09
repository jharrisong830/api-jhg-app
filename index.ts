Bun.serve({
    routes: {
        "/hello": () => {
            return new Response("Hello!");
        }
    },

    fetch(req) {
        return new Response(`Route "${req.method} ${req.url}" was not found`, {
            status: 404
        });
    }
});
