import random
from typing import List, Dict

# 問卷 URLs
SURVEYS = {
    "hotel": "https://tassel.syd1.qualtrics.com/jfe/form/SV_cCtJgUMGbUGfyxE",
    "medical": "https://tassel.syd1.qualtrics.com/jfe/form/SV_1TXCuW7dGUxH7Aa"
}


def random_survey_assignment(num_participants: int) -> List[Dict]:
    """
    隨機分派問卷給參與者
    
    Args:
        num_participants: 參與者數量
        
    Returns:
        包含參與者 ID 和分派問卷的列表
    """
    assignments = []
    
    # 確保各問卷分派數量平衡
    surveys_list = []
    hotels = num_participants // 2
    medicals = num_participants - hotels
    
    surveys_list = ["hotel"] * hotels + ["medical"] * medicals
    random.shuffle(surveys_list)
    
    for i in range(num_participants):
        survey_type = surveys_list[i]
        assignments.append({
            "participant_id": f"P{i+1:03d}",
            "survey_type": survey_type,
            "survey_url": SURVEYS[survey_type]
        })
    
    return assignments


def single_random_survey() -> Dict:
    """
    隨機選擇一個問卷
    
    Returns:
        包含問卷類型和 URL 的字典
    """
    survey_type = random.choice(list(SURVEYS.keys()))
    return {
        "survey_type": survey_type,
        "survey_url": SURVEYS[survey_type]
    }


def print_assignments(assignments: List[Dict]) -> None:
    """
    打印分派結果
    """
    print("\n=== 問卷隨機分派結果 ===\n")
    hotel_count = 0
    medical_count = 0
    
    for assignment in assignments:
        print(f"{assignment['participant_id']}: {assignment['survey_type'].upper()}")
        print(f"  {assignment['survey_url']}\n")
        
        if assignment['survey_type'] == 'hotel':
            hotel_count += 1
        else:
            medical_count += 1
    
    print(f"\n統計: 飯店 = {hotel_count}, 醫療 = {medical_count}")


if __name__ == "__main__":
    # 方式 1: 隨機分派給 10 個參與者
    print("方式 1: 隨機分派給 10 個參與者")
    assignments = random_survey_assignment(10)
    print_assignments(assignments)
    
    # 方式 2: 隨機選擇單個問卷
    print("\n\n方式 2: 隨機選擇單個問卷")
    single = single_random_survey()
    print(f"隨機問卷: {single['survey_type'].upper()}")
    print(f"URL: {single['survey_url']}")
