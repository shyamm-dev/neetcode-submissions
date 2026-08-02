class TextProcessor:
    @staticmethod
    def format_text(s1: str, s2: str = ""):
        return s1.upper() if not s2 else s1 + s2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
