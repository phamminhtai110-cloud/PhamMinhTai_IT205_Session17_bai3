import itertools

teams_list = []
match_schedule = []


def input_teams():
    """Nhập và chuẩn hóa danh sách đội tuyển."""
    global teams_list

    teams = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    cleaned_teams = [team.strip().upper() for team in teams.split(",")]

    unique_teams = []
    for team in cleaned_teams:
        if team and team not in unique_teams:
            unique_teams.append(team)

    teams_list = unique_teams

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")


def create_schedule():
    """Tạo lịch thi đấu vòng tròn một lượt."""
    global match_schedule

    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    match_schedule = [
        f"{team_a} vs {team_b}"
        for team_a, team_b in itertools.combinations(teams_list, 2)
    ]

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    for index, match in enumerate(match_schedule, start=1):
        print(f"{index}. {match}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")


def generate_match_ids():
    """Sinh mã trận đấu tự động."""
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    for index, match in enumerate(match_schedule, start=1):
        team_a, team_b = match.split(" vs ")

        code_a = f"{team_a[:3]:X<3}"
        code_b = f"{team_b[:3]:X<3}"

        match_id = f"M{index:02d}-{code_a}-{code_b}"

        print(f"Trận {index} ({match}) -> ID: {match_id}")


def main():
    """Chương trình chính."""
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            print("\n--- NHẬP DANH SÁCH ---")
            input_teams()

        elif choice == "2":
            create_schedule()

        elif choice == "3":
            generate_match_ids()

        elif choice == "4":
            print("Đóng hệ thống. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()