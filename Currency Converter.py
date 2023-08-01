print("Welcome to the Currency Converter!")


def dlr(target):
    if target == "EUR":
        return 0.91
    if target == "GBP":
        return 0.78
    if target == "JPY":
        return 142.18
    if target == "AUD":
        return 1.49


def eur(target):
    if target == "USD":
        return 1.1
    if target == "GBP":
        return 0.86
    if target == "JPY":
        return 156.79
    if target == "AUD":
        return 1.64


def gb(target):
    if target == "EUR":
        return 1.17
    if target == "USD":
        return 1.29
    if target == "JPY":
        return 182.99
    if target == "AUD":
        return 1.92


def jp(target):
    if target == "EUR":
        return 0.0064
    if target == "GBP":
        return 0.0055
    if target == "USD":
        return 0.0070
    if target == "AUD":
        return 0.010


def ad(target):
    if target == "EUR":
        return 0.61
    if target == "GBP":
        return 0.52
    if target == "JPY":
        return 95.39
    if target == "USD":
        return 0.67


print("Available Currencies:")
print("1. USD - United States Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound Sterling")
print("4. JPY - Japanese Yen")
print("5. AUD - Australian Dollar")

amount = int(input("Enter the amount to convert: "))
source = str(input("Enter the source currency code (e.g., USD): "))
target = str(input("Enter the target currency code (e.g., EUR): "))

if (
    source == "USD"
    and target == "EUR"
    or target == "GBP"
    or target == "JPY"
    or target == "AUD"
):
    convert = amount * 1 * dlr(target)
if (
    source == "EUR"
    and target == "USD"
    or target == "GBP"
    or target == "JPY"
    or target == "AUD"
):
    convert = amount * 1 * eur(target)
if (
    source == "GBP"
    and target == "EUR"
    or target == "USD"
    or target == "JPY"
    or target == "AUD"
):
    convert = amount * 1 * gb(target)

if (
    source == "JPY"
    and target == "EUR"
    or target == "GBP"
    or target == "USD"
    or target == "AUD"
):
    convert = amount * 1 * jp(target)
if (
    source == "AUD"
    and target == "EUR"
    or target == "GBP"
    or target == "JPY"
    or target == "USD"
):
    convert = amount * 1 * ad(target)


print(f"Converted Amount: {convert} {target}")
