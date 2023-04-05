import math

def entropy(pos, neg):
  prob_pos = prob(pos, pos+neg)
  prob_neg = prob(neg, pos+neg)
  return - (dist_prob(prob_pos) + dist_prob(prob_neg))

def dist_prob(prob):
  if prob == 0:
    return 0
  return prob * math.log2(prob)

def prob(qtd, total):
  return qtd/total

def ganho(S, prob_v1, entropy_v1, prob_v2, entropy_v2):
  return S - (prob_v1*entropy_v1 + prob_v2*entropy_v2)
if __name__ == "__main__":
  print("entropia base")
  print(entropy(8, 12))
  print("ganho de informacao Age (adult, child)")
  print(ganho(0.97, prob(12, 20), entropy(8, 4), prob(8, 20), entropy(0, 8)))
  print("ganho de informacao Act (stretch, dip)")
  print(ganho(0.97, prob(12, 20), entropy(8, 4), prob(8, 20), entropy(0, 8)))
  print("ganho de informacao Size (small, large)")
  print(ganho(0.97, prob(10, 20), entropy(4, 6), prob(10, 20), entropy(4, 6)))
  print("ganho de informacao Color (yellow, purple")
  print(ganho(0.97, prob(10, 20), entropy(4, 6), prob(10, 20), entropy(4, 6)))

print("********************************************")
print("entropia da base")
print(entropy(8, 4))
print("ganho de informacao ACT" (strectch, dip))
print(ganho(0.92, prob(8, 12), entropy(8, 0), prob(4, 12), entropy(0, 4)))\n",
print("ganho de informacao Size" (small, large))
print(ganho(0.92, prob(6, 12), entropy(4, 2), prob(6, 12), entropy(4, 2)))\n",
print("ganho de informacao", Color (yellow, purple))
print(ganho(0.92, prob(6, 12), entropy(4, 2), prob(6, 12), entropy(4, 2)))
