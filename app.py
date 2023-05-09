from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from adres import generate_addresses
from isimsoyisim import generate_names

app = FastAPI()


class AddressRequest(BaseModel):
    number: int
    region: str


class AddressListResponse(BaseModel):
    addresses: dict


class NamesRequest(BaseModel):
    number: int
    region: str


class NamesListResponse(BaseModel):
    names: list


@app.post("/generate_address_list/")
def generate_address_list(request: AddressRequest):
    try:
        address_list = generate_addresses(country=request.region, num_addresses=request.number)

    except:
        return HTTPException(status_code=400, detail=f"{request.region} is not a valid country code.")
    return {"addresses": address_list}


@app.post("/generate_names/")
def generate_person_list(request: NamesRequest):
    try:
        name_list = generate_names(country=request.region, num_names=request.number)

    except:
        raise HTTPException(status_code=500, detail=f"{request.region} is not a valid country code.")
    return {"names": name_list}
