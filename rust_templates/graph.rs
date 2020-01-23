fn dfs(edges : &Vec<Vec<u32>>, mut visited : &mut Vec<bool>, cur : u32, end : u32) -> bool {
    if cur == end {
        return true;
    }
    if visited[cur as usize] {
        return false;
    }
    visited[cur as usize] = true;
    for next in &edges[cur as usize] {
        let ret = dfs(&edges, &mut visited, *next, end);
        if ret {
            return true;
        }
    }
    return false;
}

fn bfs(edges : Vec<Vec<usize>>, stt : usize) -> Vec<i32> {
    let mut v : Vec<i32> = vec!(-1;edges.len());
    let mut que = std::collections::VecDeque::new();
    que.push_back(stt);
    v[stt] = 0;
    while !que.is_empty() {
        let x : usize = que.pop_front().unwrap();
        for next in edges[x].iter() {
            if v[*next] == -1 {
                v[*next] = v[x] + 1;
                que.push_back(*next);
            }
        }
    }
    return v;
}
