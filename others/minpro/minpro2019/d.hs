import Data.Traversable
import Data.List

main = do
  t <- read <$> getLine
  ps <- for [1..t] $ \x ->
    read <$> getLine
  putStrLn . show $ solve ps

solve ps =
  let (a,b,c,d,e) = dp ps (0,0,0,0,0)
  in minimum [a,b,c,d,e]

dp :: [Int] -> (Int,Int,Int,Int,Int) -> (Int,Int,Int,Int,Int)
dp [] (n,d,s,t,u) = (n,d,s,t,u)
dp (x:xs) (n,d,s,t,u) =
  let n2 = n + x
      d2 = d + (oneif odd x)
      s2 = s + (oneif even x)
      t2 = t + (oneif odd x)
      u2 = u + x
  in dp xs (n2,
      minimum [n2,d2],
      minimum [n2,d2,s2],
      minimum [n2,d2,s2,t2],
      minimum [n2,d2,s2,t2,u2])

oneif t x = if t x then 1 else 0
