import Data.Traversable
import Data.List

main = do
  n:m:xs <- map read . words <$> getLine
  ps <- for [1..n] $ \x -> do
    sort . tail . map read . words <$> getLine
  putStrLn . show $ solve'' 1 m ps

solve'' :: Int -> Int -> [[Int]] -> Int
solve'' k m ps
  | k > m = 0
  | otherwise =
      let (res, next) = oneStep k ps
      in (if (and res) then 1 else 0) + solve'' (k+1) m next

oneStep k ps =
  unzip $ map (\p -> if (if null p then False else head p == k) then 
                       (True, if null p then [] else tail p)
                     else (False, p)) ps
