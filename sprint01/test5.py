# task 5 gemini (notme)

original_text = input("Введите сообщение: ")
len_was = len(original_text)
cleaned_text = " ".join(original_text.split())
if not cleaned_text:
    print("Пустое сообщение")
else:
    cleaned_text = cleaned_text[0].upper() + cleaned_text[1:]
    if cleaned_text[-1] not in [".", "!", "?", "…"]:
        cleaned_text = cleaned_text + "."
    len_became = len(cleaned_text)
    print(cleaned_text)
    print(f"Символов было: {len_was}, стало: {len_became}")




























