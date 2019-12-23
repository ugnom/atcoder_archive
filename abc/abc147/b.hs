import Data.List

import Control.Monad
main = do
  s <- getLine
  putStrLn . show $ solve s

solve :: String -> Int
solve xs = (inSolve xs (reverse xs)) `div` 2

inSolve [] [] = 0
inSolve (x:xs) (y:ys) = (if x /= y then 1 else 0) + (inSolve xs ys)
