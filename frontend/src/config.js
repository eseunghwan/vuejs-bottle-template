
module.exports = {
    register: (v) => {
        v.prototype.$fn = `http://${window.location.hostname}:${window.location.port}/fn`;
    }
};
