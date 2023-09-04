
import felix
import elli
import yash
import diana

e = elli.get_name()
f = felix.get_name()
y = yash.get_name()
d = diana.get_name()

paragraph1 = felix.paragraph_one_felix(d,e,f,y)
paragraph2 = diana.paragraph2_diana(d,e,f,y)
paragraph3 = elli.paragraph3_elli(d,e,f,y)
paragraph4 = yash.paragraph_4_yash(d,e,f,y)
paragraph5 = felix.paragraph_five_felix(d,e,f,y)
paragraph6 = diana.paragraph6_diana(d,e,f,y)
paragraph7 = elli.paragraph7_elli(d,e,f,y)
paragraph8 = yash.paragraph_8_yash(d,e,f,y)
paragraph9 = felix.paragraph_nine_felix(d,e,f,y)
paragraph10 = diana.paragraph10_diana(d,e,f,y)
paragraph11 = elli.paragraph11_elli(d,e,f,y)
paragraph12 = yash.paragraph_12_yash(d,e,f,y)


def team_names():
    return f"This is Team Bike to the Future. We are: {f}, {e}, {y}, {d}\n\n {paragraph1} {paragraph2} {paragraph3} {paragraph4}\n\n {paragraph5} {paragraph6} {paragraph7} {paragraph8}\n\n {paragraph9} {paragraph10} {paragraph11} {paragraph12}"


if __name__ == "__main__":
    team_name = team_names()
    print(team_name)