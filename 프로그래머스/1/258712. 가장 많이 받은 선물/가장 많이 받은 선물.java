import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int len = friends.length;
        // 사람 : (선물 준사람 : 개수)
        Map<String, Map<String, Integer>> giftMap = new HashMap<>();
        setGiftMap(giftMap, friends);
        
        // 빠른 검색 위한 사람 인덱스 위치 저장
        Map<String, Integer> friendsIdx = new HashMap<>();
        for (int i = 0; i < len; i++) {
            friendsIdx.put(friends[i], i);
        }
        // 선물 지수 기록 배열
        int[] giftDegree = new int[len];
        
        // gifts 정보로 누가 누구한테 몇개 받았고 선물 지수 몇인지 기록
        recordGiftInfo(gifts, friendsIdx, giftDegree, giftMap);
        
        // 다음달 받는 선물 수 저장 배열
        int[] nextGift = new int[len];
        // 다음달 받을 선물 주고받기 계산 끝낸 경우 저장
        Set<String> complete = new HashSet<>();
        
        // 다음달 선물 정산
        calculateNextMonthGifts(
            friends,
            giftMap,
            giftDegree,
            nextGift,
            complete,
            friendsIdx
        );
        
        return getMaxCount(nextGift);
    }
    
    private void setGiftMap(
        Map<String, 
        Map<String, Integer>> giftMap, 
        String[] friends
    ) {
        for (String friend : friends) {
            // 사람 세팅
            giftMap.put(friend, new HashMap<>());
            for (String giver : friends) {
                if (!friend.equals(giver)) {
                    // 선물 준사람 개수 0으로 세팅
                    giftMap.get(friend).put(giver, 0);
                }
            }
        }        
    }
    
    private void recordGiftInfo(
        String[] gifts, 
        Map<String, Integer> friendsIdx, 
        int[] giftDegree, 
        Map<String, Map<String, Integer>> giftMap
    ) {
        for (String gift : gifts) {
            String[] record = gift.split(" ");
            String giver = record[0];
            String getter = record[1];
            int giverIdx = friendsIdx.get(giver);
            int getterIdx = friendsIdx.get(getter);
            giftDegree[giverIdx]++;
            giftDegree[getterIdx]--;
            giftMap.get(getter).put(giver, giftMap.get(getter).get(giver) + 1);
        }      
    }
    
    private void calculateNextMonthGifts(
        String[] friends,
        Map<String, Map<String, Integer>> giftMap,
        int[] giftDegree,
        int[] nextGift,
        Set<String> complete,
        Map<String, Integer> friendsIdx
    ){
        for (String friend : friends) {
            for (String giver : friends) {
                if (friend.equals(giver))
                    continue;
                // 다음달 선물 정산 완료 여부 확인
                String checkComplete = friend + giver;
                if (complete.contains(checkComplete))
                    continue;
                // friend가 giver한테 받은 선물 수
                int getCount = giftMap.get(friend).get(giver);
                // friend가 giver한테 준 선물 수
                int giveCount = giftMap.get(giver).get(friend);
                // friend와 giver의 idx
                int friendIdx = friendsIdx.get(friend);
                int giverIdx = friendsIdx.get(giver);
                // 선물 주고 받은 적 없는 사이인 경우 or 선물 주고 받은 수 같은 사이인 경우
                // 선물 지수가 큰 사람이 받음(같으면 서로 안받음)
                if ((giveCount == 0 && getCount == 0) || (giveCount == getCount)) {
                    // friend와 giver의 선물 지수
                    int friendDegree = giftDegree[friendIdx];
                    int giverDegree = giftDegree[giverIdx];
                    if (friendDegree > giverDegree)
                        nextGift[friendIdx]++;
                    else if (friendDegree < giverDegree)
                        nextGift[giverIdx]++;
                }
                // 선물 주고 받은 사이(받은 수 다른 경우)
                else {
                    // friend가 giver한테 더 많이 준 경우
                    if (giveCount > getCount) 
                        nextGift[friendIdx]++;
                    else
                        nextGift[giverIdx]++;
                }
                // 다음달 선물 주고 받기 정산 완료
                String complete1 = friend + giver;
                String complete2 = giver + friend;
                complete.add(complete1);
                complete.add(complete2);
            }
        }
    }
    
    private int getMaxCount(int[] nextGift) {
        int maxCount = 0;
        for (int count : nextGift) {
            if (count > maxCount)
                maxCount = count;
        }
        return maxCount;
    }
}