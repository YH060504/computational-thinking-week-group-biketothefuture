
import felix
import elli
import yash
import diana

e = elli.get_name()
f = felix.get_name()
y = yash.get_name()
d = diana.get_name()

paragraph1 = felix.paragraph_one_felix()
paragraph2 = diana.paragraph2_diana()
paragraph3 = elli.paragraph3_elli()
paragraph4 = yash.paragraph_4_yash()
paragraph5 = felix.paragraph_five_felix()
paragraph6 = diana.paragraph6_diana()
paragraph7 = elli.paragraph7_elli()
paragraph8 = yash.paragraph_8_yash()
paragraph9 = felix.paragraph_nine_felix()
paragraph10 = diana.paragraph10_diana()
paragraph11 = elli.paragraph11_elli()
paragraph12 = yash.paragraph_12_yash()


def team_names():
    return f"This is Team Bike to the Future. We are: {f}, {e}, {y}, {d}\n\n {paragraph1} {paragraph2} {paragraph3} {paragraph4}\n\n {paragraph5} {paragraph6} {paragraph7} {paragraph8}\n\n {paragraph9} {paragraph10} {paragraph11} {paragraph12}"


if __name__ == "__main__":
    team_name = team_names()
    print(team_name)
