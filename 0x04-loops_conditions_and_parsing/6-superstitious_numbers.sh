#!/usr/bin/env bash
# displays numbers from 1 to 20 and:
# displays 4 and then bad luck from China for the 4th loop iteration
# displays 9 and then bad luck from Japan for the 9th loop iteration
# displays 17 and then bad luck from Italy for the 17th loop iteration

COUNT=1
while [ $COUNT -lt 21 ]; do
    echo "$COUNT"
    case $COUNT in
    4)
        echo "bad luck from China"
    ;;
    9) echo "bad luck from Japan"
      ;;
      17) echo "bad luck from Italy"
      ;;
    esac
    ((COUNT++))
done
