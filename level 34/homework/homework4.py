#შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს. ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში
#  თითოეული სიმბოლოს რაოდენობა და ჩაამატოს ახალ სიაში(ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა 
# ჩაამატოთ. მგალითად თუ string-ში 5 "a" გვხვდება, რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ,
#  მაგრამ სხვა სიმბოლოც თუ გვხვდება იგივე რაოდენობით, მას ვამატებთ ჩვეულებრივ). 
# საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ

def my_function(text):
    counts = [text.count(i) for i in set(text)]
    return sorted(counts)

text = "aabbbccccdddddddggggggssss"
print(my_function(text))