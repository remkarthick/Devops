# Redis Setup in WSL (Ubuntu)

This guide explains how to install, configure, and manage Redis in WSL (Ubuntu).

---

## 1. Install Redis

```bash
sudo apt install redis-server -y
```

---

## 2. Start Redis service

```bash
sudo service redis-server start
```

Check status:

```bash
sudo service redis-server status
```

Stop service:

```bash
sudo service redis-server stop
```

---

## 3. Create Redis directory in /opt

```bash
cd /opt
sudo mkdir -p redis
```

---

## 4. Create symbolic links

```bash
sudo ln -s /usr/bin/redis-server /opt/redis/redis-server
sudo ln -s /usr/bin/redis-cli /opt/redis/redis-cli
sudo ln -s /etc/redis/redis.conf /opt/redis/redis.conf
```

Verify:

```bash
ls -l /opt/redis
```

---

## 5. Run Redis manually (background mode)

```bash
/opt/redis/redis-server --daemonize yes
```

---

## 6. Verify Redis is running

```bash
/opt/redis/redis-cli ping
```

Expected output:

```text
PONG
```

---

## 7. Stop Redis (manual mode)

```bash
/opt/redis/redis-cli shutdown
```

---

## 8. Alternative stop (service mode)

If started via service:

```bash
sudo service redis-server stop
```

---

## 9. Check Redis status

```bash
sudo service redis-server status
```

---

## 10. Manual start (no service)

```bash
/opt/redis/redis-server
```

Or with config:

```bash
/opt/redis/redis-server /opt/redis/redis.conf
```

---

## Summary

You can run Redis in two ways:

* Service mode:

  ```bash
  sudo service redis-server start
  ```

* Manual mode:

  ```bash
  /opt/redis/redis-server --daemonize yes
  ```

Both methods support:

```bash
redis-cli ping
redis-cli shutdown
```
