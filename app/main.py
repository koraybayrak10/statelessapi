from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(
    app,
    title="Stateless API",
    version="1.0",
    description="Minimal, Stateless, Docker-ready REST API",
    doc="/"  # Swagger UI
)

ns = api.namespace("api", description="API operations")

health_model = api.model("Health", {
    "status": fields.String(example="ok"),
})

echo_model = api.model("Echo", {
    "message": fields.String(example="Merhaba Dünya")
})


@ns.route("/health")
class Health(Resource):
    @ns.marshal_with(health_model)
    def get(self):
        return {"status": "ok"}


@ns.route("/echo")
class Echo(Resource):
    @ns.expect(echo_model)
    @ns.marshal_with(echo_model)
    def post(self):
        return api.payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
