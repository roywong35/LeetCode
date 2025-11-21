class Codec:
    def encode(self, strs: list[str]) -> str:
        output = []
        for s in strs:
            output.append(f"{len(s)}#{s}")
        return ''.join(output)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res

print(Codec().encode(["lint", "code", "love", "you"]))
print(Codec().decode("4#lint4#code4#love3#you"))