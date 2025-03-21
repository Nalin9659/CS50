def main():
    gretting=input ("Grettings: ").lower().strip()

    if gretting.startswith("hello"):
        print("$0")
    elif gretting.startswith("h") or gretting.startswith("hey"):
        print("$20")

    else:
        print("$100")
main()