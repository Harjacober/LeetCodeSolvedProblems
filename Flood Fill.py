def floodFill(image, sr, sc, newColor):
    if not image: return image
    m = len(image)
    n = len(image[0])
    cache = [[False]*n for _ in range(m)]

    def dfs(i,j,target,nc): 
        if not cache[i][j] and image[i][j]==target:  
            image[i][j] = nc 
            cache[i][j] = True 
            for a,b in ([i-1,j], [i,j-1], [i+1,j], [i,j+1]):
                if a>=0 and a<len(image) and b>=0 and b<len(image[0]):
                    dfs(a,b,target,nc)
        
    
    dfs(sr,sc,image[sr][sc],newColor)
    return image

if __name__ == '__main__':
    testImage = [[1,1,1],[1,1,0],[1,0,1]]
    r,c,newColor = 1,1,2
    expectedImage = [[2,2,2],[2,2,0],[2,0,1]] 
    assert(expectedImage == floodFill(testImage, r, c, newColor))