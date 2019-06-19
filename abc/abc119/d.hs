-- Multi lines of lists
import Data.Traversable
import Data.List

data BTree a = Empty | BTree (BTree a) a (BTree a)

main = do
  (a:b:q:xs) <- map read . words <$> getLine
  ss <- for [1..a] $ \x -> do
    read <$> getLine
  ts <- for [1..b] $ \x -> do
    read <$> getLine
  xs <- for [1..q] $ \x -> do
    read <$> getLine
  putStrLn . show $ solve ss ts xs

solve :: [Int] -> [Int]-> [Int] -> [Int]
solve ss ts xs =
  let stree = treeFromList ss
      ttree = treeFromList ts
  in map (solveOne stree ttree) xs

treeFromList = undefined

solveOne stree ttree x = undefined
