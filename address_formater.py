#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This is the 1st address formater in python


def formated_address(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):
    # return the newly formatted address

    # process
    if apartment_number is not None:
        address = "{0} \n{6}-{1} {2} \n{3} {4} {5}".format(
            full_name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
    else:
        address = "{0} \n{1} {2} \n{3} {4} {5}".format(
            full_name, street_number, street_name, city, province, postal_code
        )

    return address.upper()


def main():
    # get information for mail address
    # name, street number, street name etc.

    # Tell the user what this program does
    print("This program formats your address to a mailing address.")

    # input
    full_name = input("Enter your full name: ")
    apartment = input("Do you live in an apartment? (y/n): ")
    if apartment == "y":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main St, Express Pkwy…): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as abbreviation, ex ON,BC …): ")
    postal_code = input("Enter your postal code (K2F 8T2): ")
    print("")

    try:
        # convert the number variables from strings to integers
        #    aka the apartment and street numbers
        street_number_int = int(street_number)
        if apartment == "y":
            apartment_number_int = int(apartment_number)
        # call functions
        if apartment == "y":
            returned_adress = formated_address(
                full_name,
                street_number_int,
                street_name,
                city,
                province,
                postal_code,
                apartment_number_int,
            )
        else:
            returned_adress = formated_address(
                full_name, street_number_int, street_name, city, province, postal_code
            )
        # output
        print(returned_adress)
    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
