id_hash={
    
}

reported_hash={
    
}

def solution(id_list, report, k):
    for id in id_list:
        id_hash[id]=[]
        reported_hash[id]=0
    for report_item in report:
        src, dst = report_item.split(' ')
        if(dst not in id_hash[src]):
            id_hash[src].append(dst)
            reported_hash[dst]+=1
    answer = []
    for id in id_hash:
        cur_answer = 0
        for dst_id in id_hash[id]:
            if(reported_hash[dst_id]>=k):
                cur_answer+=1
        answer.append(cur_answer)
    return answer