
-- Single variable
main = do
  x <- read <$> getLine
  putStrLn . show $ solve x

solve :: Int -> Int
solve = undefined

-- Single variable yes/no
main = do
  x <- read <$> getLine
  putStrLn $ if solve x then "YES" else "NO"

solve :: Int -> Int
solve = undefined


-- 2 variables
main = do
  (x:y:xs) <- map read . words <$> getLine
  putStrLn . show $ solve x y

solve :: Int -> Int -> Int
solve = undefined

-- Multi lines of lists
import Data.Traversable
import Data.List

main = do
  t <- read <$> getLine
  ps <- for [1..t] $ \x -> do
    read <$> getLine
  putStrLn . show $ solve ps

solve :: [Int] -> Int
solve = head
