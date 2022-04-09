""" program to to get the pig string"""
def main():
    x = "this"
    x = x.split(" ")
    final = []
    for i in x:
        if i[0].lower() in ['a','e','i','o','u']:
            if len(i) >= 1:
                i = i + "way"

        else:
            if len(i) > 1:
                i = i[1:] + i[0] + "ay"
            else:
                i = i+"ay"
        final.append(i)

    print(" ".join(final))

if __name__ == "__main__":
    main()
            
