from pprint import pprint


class Gym:

    def __init__(self, name, bench, squat, deadlift):
        self.name = name
        self.bench = bench
        self.squat = squat
        self.deadlift = deadlift

    def sbd_competition(self, competitors):
        sbd_scores = {}
        for competitor in competitors:
            print(f'Привет, меня зовут {competitor.name}, хочу учавствовать в соревнованиях!')
            total_score = competitor.bench + competitor.squat + competitor.deadlift
            sbd_scores[competitor.name] = total_score

        winner = max(sbd_scores, key=sbd_scores.get)
        return winner



gym_member1 = Gym('Валера', 120, 180, 225)
gym_member2 = Gym('Дима', 115, 176, 200)
gym_member3 = Gym('Даня', 120, 200, 200)

competitors = [gym_member1, gym_member2, gym_member3]
gym = Gym('', 0, 0, 0)

winner = gym.sbd_competition(competitors)
print('Победу одержал:', winner)


def introspection_info(obj):
    info_dict = {}
    info_dict['Type'] = type(obj).__name__
    info_dict['Attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info_dict['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info_dict['Module'] = type(obj).__module__

    return info_dict

pprint(introspection_info(Gym))