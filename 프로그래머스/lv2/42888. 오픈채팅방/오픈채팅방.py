from collections import defaultdict

def solution(record):
    answer = []
    enter = '{}님이 들어왔습니다.'
    leave = '{}님이 나갔습니다.'
    ids = defaultdict(str)
    msgs = []

    for r in record:
        splits = r.split()
        act = splits[0]
        uid = splits[1]
        if act != 'Leave':
            nick = splits[2]

        if act == 'Enter':
            ids[uid] = nick
            msgs.append((uid, enter))
        elif act == 'Leave':
            msgs.append((uid, leave))
        elif act == 'Change':
            ids[uid] = nick

    for i, msg in enumerate(msgs):
        uid, msg_format = msg
        answer.append(msg_format.format(ids[uid]))
    return answer