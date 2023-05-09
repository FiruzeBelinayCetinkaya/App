from mimesis import Address


def generate_addresses(country, num_addresses):
    address = Address(locale=country)
    address_list = []
    for i in range(num_addresses):
        address_list.append(address.address())
    return address_list

