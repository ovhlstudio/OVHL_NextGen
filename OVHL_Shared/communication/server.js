class OVHLServer {
  constructor() {
    this.clients = [];
  }
  start() {
    console.log("OVHL Server Started");
    return true;
  }
}
module.exports = OVHLServer;
