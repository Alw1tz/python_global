#input
# 9563 59114 -54932 48501 -65301 -75301 65794 518 72323 -52815 -39714 65537 -55115 -22581 -32780 30204 -57857 28574 35328 -19926 -52635 -43638 149 73410 903 -58837 27817 -24007 -76410 -26990 43898 13152 -47875 68965 -18347 -33176 73664 -32552 47341 65987 -5368 -72373 51525 19516 -14954 -61254 -30279 7189 47319 -74951 67262 74683 -38589 -12588 68094 42313 8575 15911 -61693 12164 68921 62204 -54683 -58954 51170 6970 -12131 44835 54417 -44790 30822 -30950 -37163 2348 68566 27882 21093 -41712 -44929 -11587 -36663 -57666 -16904 4747 9746 -28809 -32940 -61679 67101 -14633 30485 56022 -32429 55801 77068 -61258 -17229 -15063 63576 -42811 20147 14399 6239 62983 -63253 -5195 10866 37839 33093 45937 -53747 76429 68271 9349 1176 -1982 60539 48236 16339 47641 -46397 -33176 23664 1174 -57375 20732 19915 5396 -74331 3491 42585 25816 -62110 -31176 8800 -45363 43629 -60334 72475 -3278 65603 -61271 -6848 53875 28077 74327 -28107 8616 42564 68231 -23743 76166 -44944 79920 -2660 -22320 20652 -62744 63076 26321 20747 25662 -27863 38636 74485 60936 73273 38115 -79397 65748 -45162 66206 -75522 27989 40081 32554 22317 -68025 -38830 -15119 -79794 17426 -18953 -44739 17346 58387 12941 -42001 75643 -3982 64319 16390 -58320 -43543 -24973 -63834 -62606 -31700 54281 -62004 -45951 -70881 -75798 -41474 37108 44283 71079 -20575 56257 -47751 44305 56463 49675 -54647 -68275 -12978 -76259 24666 25020 79383 -59316 9340 15774 -37636 45797 70800 -21470 63190 -40900 -47189 -78814 -6851 -38071 -74612 31674 79036 49671 22753 -21538 25928 55002 -57232 2392 24678 -31879 14116 -68300 -28139 -41218 36720 -28755 -20534 -33939 67019 21829 -68142 57819 -79641 75047 -63080 -46831 76233 10068 -4902 -78378 -38257 -5865 51292 64496 52596 -2779 39498 75364 79612 -15824 -36515 13729 -4124 15346 52510 -47404 66591 -48024 -1343 53610 53805 10514 31430 54163 5562 48350 -72667 1796 -21582 2430 3417 20161 76565 -25290 4657

array = input().split()
print(max(int(i) for i in array), " ", end="")
print(min(int(i) for i in array), " ", end="")