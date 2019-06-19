-- Multi lines of lists
import Data.Traversable
import Data.List

main = do
  t <- read <$> getLine
  ps <- for [1..t] $ \x -> do
    (\xs -> (read $ xs!!0, xs!!1)) . words <$> getLine
  putStrLn . show $ solve ps

solve :: [(Double, String)] -> Double
solve [] = 0
solve ((x,c):xs) = case c of
  "JPY" -> x + (solve xs)
  "BTC" -> 380000.0 * x + (solve xs)
