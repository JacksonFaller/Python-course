from fastapi import FastAPI

app = FastAPI(title="Inventory API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# TODO: add the inventory endpoints described in README.md.
