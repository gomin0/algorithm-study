import itertools

def solution(users, emoticons):
    # 이모티콘 할인의 가능한 모든 경우의 수 생성 (10%, 20%, 30%, 40%)
    discount_rates = [10, 20, 30, 40]
    possible_discounts = list(itertools.product(discount_rates, repeat=len(emoticons)))

    # 결과 변수 (최대 가입자 수, 최대 매출액)
    max_subscribers = 0
    max_sales = 0

    # 가능한 모든 할인 조합에 대해 계산
    for discounts in possible_discounts:
        subscribers = 0  # 현재 할인 조합에서의 가입자 수
        sales = 0  # 현재 할인 조합에서의 매출액
        
        # 각 사용자에 대해 계산
        for rate, threshold in users:
            total_purchase = 0  # 해당 사용자의 총 구매액

            # 이모티콘별로 할인 가격을 적용하여 계산
            for i, price in enumerate(emoticons):
                discount_price = price * (100 - discounts[i]) // 100  # 할인된 가격
                if discounts[i] >= rate:
                    total_purchase += discount_price  # 해당 사용자가 구매하는 가격

            # 사용자가 플러스 서비스에 가입하는지 확인
            if total_purchase >= threshold:
                subscribers += 1  # 가입자 수 증가
            else:
                sales += total_purchase  # 사용자가 구매한 금액을 매출액에 더함

        # 최적의 값으로 갱신
        if subscribers > max_subscribers or (subscribers == max_subscribers and sales > max_sales):
            max_subscribers = subscribers
            max_sales = sales

    return [max_subscribers, max_sales]