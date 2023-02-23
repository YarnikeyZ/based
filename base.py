def getInput():
    from sys import argv
    try:
        base = 2 if argv[1] == "2" else 10
        number = argv[2]
    except IndexError:
        base = 2 if input("Base (10, 2): ") == "2" else 10
        number = input(f"Number (Base {base}): ")
    return base, number

def prettifyNumbers(numbers: int, power: bool):
    prettyChars = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"] if power else ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]
    return "".join([prettyChars[int(n)] for n in list(str(numbers))])

def binaryToDecimal(binary: str):
    result = ""
    result += f"({binary}){prettifyNumbers(2, False)} = "
    decimal = 0

    for numBinary, intPower in zip(binary, range(len(binary), -1, -1)):
        result += f"({numBinary} * 2{prettifyNumbers(intPower-1, True)}){' + ' if intPower != 1 else ''}"
        decimal += int(numBinary) * (2 ** (intPower-1))
    
    result += f" = ({decimal}){prettifyNumbers(10, False)}"
    return result

def decimalToBinary(decimal: str):
    decimal = int(decimal)
    result = ""
    result += f"({decimal}){prettifyNumbers(10, False)} ="
    binary = ""

    while (int(decimal) > 0):
        remainder = int(float(decimal%2))
        result += f" {int(decimal)}:2={int(decimal//2)}({remainder})"
        binary += str(remainder)
        decimal = (decimal-remainder)/2
    
    binary = binary[::-1]
    result += f" = ({binary}){prettifyNumbers(2, False)}"
    return result

def main():
    userInput = getInput()
    print(binaryToDecimal(userInput[1]) if userInput[0] == 2 else decimalToBinary(userInput[1]))

if __name__ == "__main__":
    main()