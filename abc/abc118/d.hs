import Data.List

main = do
  (n:m:xs) <- map read. words <$> getLine
  ps <- map read . words <$> getLine
  putStrLn . show $ solve n ps

num = [2,5,5,4,5,6,3,7,6]
getCost i = num !! (i-1)

solve :: Int -> [Int] -> String
solve n ps =
  let pps = sortBy numOrder . map (\p -> (getCost p, p)) $ ps
      tc = topCond . head $ pps


numOrder (a,b) (c,d) =
  if compare a c /= EQ then
    compare a c
  else
    compare d b

solve' n (p:pps) =
  let tc = topCond n $ snd p
  in 


topCond n c = tail . reverse $ zip [n,n-c..0] [0..]
