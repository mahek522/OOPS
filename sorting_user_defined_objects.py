#Implementing selection sort on user-defined objects
#Sorting FootBaller objects based on number of goals scored
class FootBaller:
    def __init__(self, name, goals, assist):
        self.name = name
        self.goals = goals
        self.assist = assist
    def __lt__(self, other):
        return self.goals < other.goals
    def __gt__(self, other):
        return self.goals > other.goals
    def __str__(self):
        return f"{self.name}: Goals={self.goals}, Assists={self.assist}"

def sort_footballers(lst):
    n = len(lst)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
def main():
    f1 = FootBaller("Messi", 650, 359)
    f2 = FootBaller("Ronaldo", 750, 250)
    f3 = FootBaller("Neymar", 450, 125)
    f4 = FootBaller("Luis", 300, 600)
    lst = [f1, f2, f3, f4]
    sort_footballers(lst)
    for f in lst:
        print(f)
if __name__ == "__main__":
    main()