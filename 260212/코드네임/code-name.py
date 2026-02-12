MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []
for c, s in zip(codenames, scores):
    agents.append(Agent(c,s))

min_agent, min_score = '', 100
for agent in agents:
    if agent.score < min_score:
        min_agent = agent.codename
        min_score = agent.score

print(min_agent, min_score)
