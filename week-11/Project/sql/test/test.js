var supertest = require("supertest");
var should = require("should");
var chakram = require("chakram");


describe("HTTP assertions", function () {



  it("should make HTTP assertions easy", function () {
    var response = chakram.get("http://localhost:3000");
    expect(response).to.have.status(200);
    expect(response).to.have.header("content-type", "application/json");
    expect(response).not.to.be.encoded.with.gzip;
    expect(response).to.comprise.of.json({
      args: { test: "chakram" }
    });
    return chakram.wait();
  });
});
