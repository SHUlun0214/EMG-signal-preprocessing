def cut_trigger(trigger_t, trigger_v):
    trigger_action_index = [i for i, x in enumerate(trigger_v) if x == 1.0]
    trigger_action_t = []
    trigger_action_v =[]
    for i in trigger_action_index:
        trigger_action_t.append(trigger_t[i])
        trigger_action_t.append(trigger_t[i+2])
        trigger_action_v.append(trigger_v[i])
        trigger_action_v.append(trigger_v[i+2])

    return trigger_action_t, trigger_action_index, trigger_action_v