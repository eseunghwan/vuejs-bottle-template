module.exports = {
    pages: {
        Index: {
            entry: "./src/views/Index.js",
            template: "./public/view.html",
            title: "Index",
            filename: "Index.html"
        },
        Test: {
            entry: "./src/views/Test.js",
            template: "./public/view.html",
            title: "Test",
            filename: "Test.html"
        }
    }
};