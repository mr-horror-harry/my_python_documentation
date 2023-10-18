def call():
    print(f"Script executed as {__name__} ")

if __name__=="__main__":
    print("Tmp file script is run directly!")
    call()
else:
    print("Tmp file script is being imported and called!")