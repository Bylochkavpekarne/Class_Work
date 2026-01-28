print("\n-----Перший рівень-----\n")



print("\n-----Перше завдання-----\n")



text = " Why Is Arch Linux So Cool?I moved to Arch Linux from macOS a few months ago, and it feels like the only operating system I need. Everything is well documented and very easy to configure. The pacman package manager is just awesome, and together with yay, it makes it easy to install literally everything I need.The thing is, I had some experience with Ubuntu before installing Arch, and it didn’t feel as nice or comfortable. But why? Other GNU/Linux distributions have package managers as well, and they use the same configuration files, and so on.So when my friend asked me why I ended up falling in love with Arch Linux, I realized that I didn’t actually know the answer. Maybe you can answer this question?I use Arch Linux mostly for playing Roblox and Minecraft, software development in C, Python, Assembly, and Rust, and for building electrical circuits and similar things. I know I can do all of this on almost any operating system and GNU/Linux distribution, but Arch Linux still feels like a gem."
count = text.count('.') + text.count('?') + text.count('!')
print("Кількість речень у тексті: ", count)



print("\n-----Друге завдання-----\n")



s = input("Введіть текст: ")

def idk(s):
    s = s.lower()
    return s == s[::-1]

if idk(s):
    print("Tak")
else:
    print("No")



print("\n-----Другий рівень-----\n")



print("\n-----Перше завдання-----\n")



idk = "idk", "привіт", "сало", "козак", "кіт", "bylochka"
user = input("Введіть Ваш текст: ").lower()
for word in user.split():
    if word in idk:
        print(word.upper())
        break
else:
    print("Нема слів із списку")




print("\n-----Друге завдання-----\n")



user = input("Введіть Ваш текст: ")
first = user.find('!') + 1
second = user.find('@')

print = s[first:second]