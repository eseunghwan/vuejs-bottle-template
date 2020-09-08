
var host = "127.0.0.1";
var port = 47352;

module.exports = {
    register: (v) => {
        v.prototype.$fn = `http://${host}:${port}/fn`;
    }
};
