import Data.Traversable
import Data.List


main = do
  ps <- for [1..3] $ \x -> do
    map read . words <$> getLine
  putStrLn $ if solve'' ps == True then "YES" else "NO"

solve'' :: [[Int]] -> Bool
solve'' ps =
  let ss = sort $ concat ps
      counts =  map (\x -> count x ss) [1..4]
  in count 2 counts == 2 && count 1 counts == 2

count _ [] = 0
count p (x:xs) = if p == x then 1 + (count p xs) else count p xs
