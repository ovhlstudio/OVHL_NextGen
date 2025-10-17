class OVHLClient {
  constructor() {
    this.connected = false;
  }
  connect() {
    this.connected = true;
    console.log("OVHL Client Connected");
    return true;
  }
}
module.exports = OVHLClient;
