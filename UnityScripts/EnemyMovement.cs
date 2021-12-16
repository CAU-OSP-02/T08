using UnityEngine;

public class EnemyMovement : MonoBehaviour
{
    private LayerMask tileLayer;
    private float rayDistance = 0.55f;
    private Vector2    moveDirection = Vector2.right;
    private Direction  direction = Direction.Right;

    private Movement2D movement2D;

    private void Awake()
    {
        tileLayer = 1 << LayerMask.NameToLayer("Tile");

        movement2D = GetComponent<Movement2D>();

        SetMoveDirectionByRandom();
    }

    private void Update()
    {
        RaycastHit2D hit = Physics2D.Raycast(transform.position, moveDirection, rayDistance, tileLayer);

        if (hit.transform == null)
        {
            movement2D.MoveTo(moveDirection);
        }
        else
        {
            SetMoveDirectionByRandom();
        }
    }

    private void SetMoveDirectionByRandom()
    {
        direction      = (Direction)Random.Range(0, 4);
        moveDirection  = Vector3FromEnum(direction);
    }

    private Vector3 Vector3FromEnum(Direction state)
    {
        Vector3 direction = Vector3.zero;

        switch (state)
        {
            case Direction.Up:    direction = Vector3.up;    break;
            case Direction.Left:  direction = Vector3.left;  break;
            case Direction.Right: direction = Vector3.right; break;
            case Direction.Down:  direction = Vector3.down;  break;
        }

        return direction;
    }
}
